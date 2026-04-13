import re

path = "tehi-theme/front-page.php"
with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# Replace $hero_args, $hot_args, $rank_args to handle missing _views gracefully.
# Instead of purely meta_value_num which requires the key, we order by modified/date as a fallback if views fail.
# A robust WP_Query for "views or 0":
fallback_query = """[
        'post_type' => 'truyen',
        'posts_per_page' => {LIMIT},
        'meta_query' => [
            'relation' => 'OR',
            'has_views' => ['key' => '_views', 'compare' => 'EXISTS'],
            'no_views'  => ['key' => '_views', 'compare' => 'NOT EXISTS']
        ],
        'orderby' => [
            'has_views' => 'DESC',
            'date' => 'DESC'
        ]
    ]"""

# 1. Hero
hero_fallback = fallback_query.replace("{LIMIT}", "4")
code = re.sub(r"\$hero_args\s*=\s*\[(.*?)meta_key.*?\];", f"$hero_args = {hero_fallback};", code, flags=re.DOTALL)

# 2. Hot (Editor Choice)
hot_fallback = fallback_query.replace("{LIMIT}", "3")
code = re.sub(r"\$hot_args\s*=\s*\[(.*?)meta_key.*?\];", f"$hot_args = {hot_fallback};", code, flags=re.DOTALL)

# 3. Rank
rank_fallback = fallback_query.replace("{LIMIT}", "10")
code = re.sub(r"\$rank_args\s*=\s*\[(.*?)meta_key.*?\];", f"$rank_args = {rank_fallback};", code, flags=re.DOTALL)


# Also ensure Hero slider doesn't collapse if there are NO posts at all or only 1 post.
# (CSS handles it mostly, but let's make sure).

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Queries fixed!")
