async (page) => {
  // Run Playwright MCP from the GRA checkout root (see README.md).
  const screenshotDir = 'experiments/issue-7/screenshots';
  const baseUrl = 'http://127.0.0.1:8768/';
  const errors = [];
  await page.unroute('**/data/a-in-kit.json');
  page.on('pageerror', error => errors.push(error.message));
  await page.setViewportSize({width:1280,height:960});
  await page.goto(baseUrl + '#processes', {waitUntil:'domcontentloaded'});
  await page.reload({waitUntil:'domcontentloaded'});
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);
  await page.waitForFunction(() => document.querySelectorAll('.testkit-step').length === 35);
  const steps = await page.evaluate(async () => (await (await fetch('data/a-in-kit.json')).json()).steps);
  if (steps.length !== 24) throw new Error('Expected 24 steps');
  if (await page.locator('.process-help').count() !== 1) throw new Error('Help form changed');
  if (await page.locator('.testkit-step-layout').count() !== 35) throw new Error('Card form changed');
  for (const step of steps) {
    const card = page.locator(`[data-ain-step="${step.id}"]`);
    if (await card.locator('.testkit-more a[href^="#prompt="]').count() < 2) throw new Error('Archive links missing: '+step.id);
    if (!await card.locator('.prompt-links a').count()) throw new Error('Step links missing: '+step.id);
    if (await card.locator('.testkit-prompt-text').textContent() !== step.prompt) throw new Error('Preview differs: '+step.id);
    const expected = `<!-- mango-bcreq-${step.id.toLowerCase()}-stepwise · ${step.id} ${step.name} -->\n\n${step.prompt}`;
    await card.locator('.testkit-copy').click();
    await page.waitForFunction(async text => (await navigator.clipboard.readText()) === text, expected);
  }
  // Legacy stages retain the same version switcher and preview/copy behavior.
  await page.locator('[data-process-tab="g2"]').click();
  const legacy = page.locator('.testkit-group[data-group="g2"] .testkit-step').first();
  const editions = legacy.locator('[data-testkit-edition]');
  if (await editions.count() !== 2) throw new Error('Legacy comparison lost');
  const before = await legacy.locator('.testkit-prompt-text').textContent();
  await editions.nth(1).click();
  if (await legacy.locator('.testkit-prompt-text').textContent() === before) throw new Error('Legacy edition failed');
  await editions.nth(0).click();
  await page.locator('[data-process-tab="g1"]').click();
  await page.waitForFunction(() => document.querySelector('#bcreq-testkit-g2').hidden && !document.querySelector('#bcreq-testkit-g1').hidden);
  if (await page.locator('.testkit-step:visible').count() !== 25) throw new Error('Group count differs');
  await page.reload({waitUntil:'domcontentloaded'}); // Reset toast/scroll for reproducible screenshots.
  await page.waitForFunction(() => document.querySelectorAll('[data-ain-step]').length === 24);
  const card = page.locator('[data-ain-step="AIN-01"]');
  const scrollToCard = async () => {
    await card.evaluate(el => {
      const header = document.querySelector('.topbar').getBoundingClientRect().height;
      window.scrollTo({top:el.getBoundingClientRect().top + window.scrollY - header - 16, behavior:'instant'});
    });
  };
  await scrollToCard();
  await page.screenshot({path:screenshotDir+'/candidate-2.8.5-desktop.png'});
  await page.setViewportSize({width:390,height:844});
  await scrollToCard();
  if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth)) throw new Error('Mobile overflow');
  await card.screenshot({path:screenshotDir+'/candidate-2.8.5-mobile.png'});
  // A failed data load has explicit feedback and a normal reload recovers.
  await page.route('**/data/a-in-kit.json', route => route.abort());
  await page.reload({waitUntil:'domcontentloaded'});
  await page.waitForFunction(() => document.querySelector('#bcreq-testkit-summary').textContent.includes('Данные не загрузились'));
  await page.unroute('**/data/a-in-kit.json');
  await page.reload({waitUntil:'domcontentloaded'});
  await page.waitForFunction(() => document.querySelectorAll('[data-ain-step]').length === 24);
  await page.locator('[data-ain-step="AIN-01"] .testkit-copy').click();
  await page.waitForFunction(async text => (await navigator.clipboard.readText()).endsWith(text), steps[0].prompt);
  const routes = ['about','catalog','standards','processes','dashboard','glossary'];
  await page.setViewportSize({width:1280,height:960});
  for (const route of routes) {
    await page.locator(`[data-nav="${route}"]`).click();
    await page.waitForFunction(r => location.hash === '#'+r, route);
    await page.waitForFunction(r => document.querySelector(`[data-nav="${r}"]`).dataset.active === 'true', route);
    if (!await page.locator(`[data-page="${route}"]:visible`).count()) throw new Error('Page hidden: '+route);
  }
  await page.goto(baseUrl+'#catalog', {waitUntil:'domcontentloaded'});
  const select = async token => page.locator('[data-filter-token]').evaluateAll(
    (els,token)=>els.find(e=>e.dataset.filterToken===token).click(), token);
  if (await page.locator('.prompt-card').count() !== 39) throw new Error('Active catalogue');
  await select('family:archive');
  if (await page.locator('.prompt-card').count() !== 18) throw new Error('Archive catalogue');
  await select('process:A-IN · Приём задачи');
  await page.locator('#search-input').fill('2.7.0');
  await page.waitForFunction(()=>document.querySelectorAll('.prompt-card').length===4);
  const archives = await page.evaluate(async()=>
    (await (await fetch('data/prompts.json')).json()).prompts.filter(p=>p.archiveInfo));
  if (archives.length !== 4) throw new Error('Archive count');
  for (const prompt of archives) {
    await page.locator(`[data-copy-id="${prompt.id}"]`).first().click();
    await page.waitForFunction(async text=>(await navigator.clipboard.readText())===text,
      `<!-- ${prompt.id} -->\n\n${prompt.body}`);
  }
  await page.locator('#search-input').fill('no-such-id');
  await page.goto(baseUrl+'#prompt='+archives[0].id, {waitUntil:'domcontentloaded'});
  await page.waitForFunction(()=>document.querySelectorAll('.prompt-card').length===1);
  for (const id of ['AIN-02','AIN-14','AIN-24']) {
    await page.goto(baseUrl+'#processes?ain='+id, {waitUntil:'domcontentloaded'});
    await page.waitForFunction(id=>!document.querySelector(`[data-ain-step="${id}"]`).closest('.testkit-group').hidden,id);
  }
  for (const section of ['1','2','ttz','9']) {
    await page.goto(baseUrl+'#standards?section='+section, {waitUntil:'domcontentloaded'});
    const target=page.locator(section==='ttz'?'#standard-ttz':section==='9'?'#standard-industry':'#standard-'+section);
    if (!await target.isVisible()) throw new Error('Standard hidden: '+section);
  }
  if (errors.length) throw new Error(errors.join('\n'));
  return {routes, cards:35,ain:24,copies:24,archiveCopies:4,archiveSearch:true,deepLinks:true,standardLinks:true,
    byteEqual:true,previewEqual:true,legacyEditions:true,
    sameCardForm:true,mobileOverflow:false,errorReload:true,pageErrors:errors};
}
