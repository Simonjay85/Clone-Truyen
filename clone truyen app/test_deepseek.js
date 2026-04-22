const fs = require('fs');

async function test() {
  const db = JSON.parse(fs.readFileSync('data/mcore_db.json', 'utf8'));
  const apiKey = db.deepseekKey;
  
  if (!apiKey) {
      console.log('NO DEEPSEEK KEY');
      return;
  }
  
  console.log("Testing DeepSeek Key...");
  const payload = {
      model: 'deepseek-chat',
      messages: [{ role: 'user', content: 'Ping' }],
      max_tokens: 10
  };
  
  const res = await fetch('https://api.deepseek.com/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify(payload)
  });
  
  const text = await res.text();
  console.log(`Status: ${res.status}`);
  console.log(`Response: ${text}`);
}

test();
