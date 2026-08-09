```ruby
Milkeclair.profile do |me|
 me.description do
  intro "ひよっこ"
  enjoy "自分が欲しいものを作ります"
  good  "ほんのちょっとだけRubyができる"
 end

 me.stack do
  languages  :ruby, :shell_script
  frameworks :ruby_on_rails
 end

 me.interests :dsl, :vanilla_coding, :domain_modeling
end
```

<details>
<summary>definitions</summary>

```ruby
class Milkeclair
 include Singleton

 attr_accessor :descriptions, :fav_languages, :fav_frameworks, :interests

 def initialize
  @descriptions   = []
  @fav_languages  = []
  @fav_frameworks = []
  @interests      = []
 end

 def self.profile(&block) = block.call(instance)

 def description(&block) = instance_eval(&block)
 alias_method :stack, :description

 def intro(text) = self.descriptions << text
 alias_method :enjoy, :intro
 alias_method :good,  :intro

 def languages(*)  = self.fav_languages  = [*]
 def frameworks(*) = self.fav_frameworks = [*]
 def interests(*)  = self.interests      = [*]
end
```
</details>

[![stats](https://github-readme-stats.vercel.app/api/wakatime?username=milkeclair&layout=compact&disable_animations=true&langs_count=20&card_width=1010&bg_color=262c36&hide_border=true&text_color=d1d7e0&title_color=d1d7e0)](https://github.com/anuraghazra/github-readme-stats)

<!--START_SECTION:waka-->
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C677%20hrs%2051%20mins-blue?style=flat)

![AI Code Time](http://img.shields.io/badge/AI%20Code%20Time-419%20hrs%2058%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-625.68%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1391 commits        █████░░░░░░░░░░░░░░░░░░░░   21.43 % 
🌆 Daytime                1541 commits        ██████░░░░░░░░░░░░░░░░░░░   23.74 % 
🌃 Evening                1821 commits        ███████░░░░░░░░░░░░░░░░░░   28.05 % 
🌙 Night                  1738 commits        ███████░░░░░░░░░░░░░░░░░░   26.78 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   814 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.54 % 
Tuesday                  885 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.63 % 
Wednesday                627 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.66 % 
Thursday                 823 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.68 % 
Friday                   1247 commits        █████░░░░░░░░░░░░░░░░░░░░   19.21 % 
Saturday                 721 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.11 % 
Sunday                   1374 commits        █████░░░░░░░░░░░░░░░░░░░░   21.17 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Markdown                 10 hrs 7 mins       ██████████████░░░░░░░░░░░   54.43 % 
Other                    4 hrs 8 mins        ██████░░░░░░░░░░░░░░░░░░░   22.24 % 
Python                   1 hr 48 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   09.70 % 
JSON                     1 hr 23 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   07.45 % 
Ruby                     49 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   04.42 % 

💻 Operating System: 
WSL                      18 hrs 36 mins      █████████████████████████   100.00 % 
```

🤖 **AI Coding This Week** 

```text
⏱ AI Coding Time: 15 hrs 39 mins (84.13%)

✍️ 990 lines written by AI, 49 lines written by hand (95.28% AI-written)

🔤 392,131,271 Input Tokens, 1,168,653 Output Tokens

💵 $934.07 Estimated AI Cost This Week

🧠 46 AI Sessions, 886 AI Prompts

GPT                      990 lines           █████████████████████████   100.00 % 

🔎 AI Coding Insights:
🤖 AI-Driven — 95.28% of written lines came from AI
📚 Verbose Prompter — average 5,956 characters per prompt
🔁 Iterative Prompter — average 19 prompts per session
🚀 High AI Trust — 15.96% of changed lines were hand-edited
```

**I Mostly Code in Ruby** 

```text
Ruby                     8 repos             ████████████░░░░░░░░░░░░░   50.00 % 
JavaScript               3 repos             █████░░░░░░░░░░░░░░░░░░░░   18.75 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   12.50 % 
Java                     1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.25 % 
Shell                    1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.25 % 
```




 Last Updated on 09/08/2026 18:45:34 UTC
<!--END_SECTION:waka-->
