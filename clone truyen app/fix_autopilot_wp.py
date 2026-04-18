import re

path = "src/hooks/useAutoPilotEngine.ts"
with open(path, "r") as f:
    c = f.read()

# Replace creation logic
create_find = '''          if (!wpPostId) {
            const wpRes = await callWordPress({
              wpUrl, wpUser, wpAppPassword,
              endpoint: 'truyen',
              method: 'POST',
              payload: {
                title: activeItem.title,
                content: activeItem.bible?.overallSizzle || activeItem.prompt,
                status: 'draft'
              }
            });
            wpPostId = wpRes.id;
            updateQueueItem(activeItem.id, { wpPostId });
          }'''

create_rep = '''          if (!wpPostId) {
            if (wpUrl && wpUser && wpAppPassword) {
              const wpRes = await callWordPress({
                wpUrl, wpUser, wpAppPassword,
                endpoint: 'truyen',
                method: 'POST',
                payload: {
                  title: activeItem.title,
                  content: activeItem.bible?.overallSizzle || activeItem.prompt,
                  status: 'draft'
                }
              });
              wpPostId = wpRes.id;
            } else {
              // Bỏ qua WP, dùng ID ảo để tiếp tục chạy Local
              wpPostId = Date.now();
            }
            updateQueueItem(activeItem.id, { wpPostId });
          }'''

c = c.replace(create_find, create_rep)

# Replace writing logic (publish chapter)
# Finding: 
#           await callWordPress({
#             wpUrl, wpUser, wpAppPassword,
#             endpoint: 'chuong',
#             method: 'POST',

write_find = '''          await callWordPress({
            wpUrl, wpUser, wpAppPassword,
            endpoint: 'chuong',
            method: 'POST',
            payload: {
              title: `Chương ${targetEpisode}: ${chapterContent.substring(0, 50)}...`,
              content: chapterContent,
              status: 'publish',
              truyen: activeItem.wpPostId
            }
          });'''

write_rep = '''          if (wpUrl && wpUser && wpAppPassword) {
            await callWordPress({
              wpUrl, wpUser, wpAppPassword,
              endpoint: 'chuong',
              method: 'POST',
              payload: {
                title: `Chương ${targetEpisode}: ${chapterContent.substring(0, 50)}...`,
                content: chapterContent,
                status: 'publish',
                truyen: activeItem.wpPostId
              }
            });
          }'''

c = c.replace(write_find, write_rep)

with open(path, "w") as f:
    f.write(c)
print("Bypassed WP!")
