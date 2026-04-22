fetch('https://api.deepseek.com/chat/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer test' // We just need to see if it's 401 Unauthorized or 404
  },
  body: JSON.stringify({model: 'deepseek-chat', messages: []})
}).then(res => { console.log("Status:", res.status); return res.json(); }).then(data => console.log(data)).catch(console.error);
