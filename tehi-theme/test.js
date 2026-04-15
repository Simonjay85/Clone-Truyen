const { JSDOM } = require('jsdom');
const dom = new JSDOM(`
<body>
    <div class="studio-layout">
        <aside class="sidebar">
            <div id="panel">
                </div>
                </div> <!-- EXTRA -->
            </div> <!-- EXTRA -->
            <div id="panel2"></div>
        </aside>
        <main></main>
    </div>
</body>
`);
console.log(dom.window.document.body.innerHTML);
