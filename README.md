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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C663%20hrs%2030%20mins-blue?style=flat)

![AI Code Time](http://img.shields.io/badge/AI%20Code%20Time-404%20hrs%2018%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-611.90%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1391 commits        █████░░░░░░░░░░░░░░░░░░░░   21.45 % 
🌆 Daytime                1541 commits        ██████░░░░░░░░░░░░░░░░░░░   23.76 % 
🌃 Evening                1819 commits        ███████░░░░░░░░░░░░░░░░░░   28.05 % 
🌙 Night                  1735 commits        ███████░░░░░░░░░░░░░░░░░░   26.75 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   814 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.55 % 
Tuesday                  885 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.64 % 
Wednesday                627 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.67 % 
Thursday                 823 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.69 % 
Friday                   1245 commits        █████░░░░░░░░░░░░░░░░░░░░   19.20 % 
Saturday                 718 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.07 % 
Sunday                   1374 commits        █████░░░░░░░░░░░░░░░░░░░░   21.18 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Markdown                 12 hrs 20 mins      ███████████████░░░░░░░░░░   59.33 % 
Other                    3 hrs 52 mins       █████░░░░░░░░░░░░░░░░░░░░   18.64 % 
JavaScript               1 hr 44 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   08.35 % 
INI                      43 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   03.50 % 
Python                   41 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   03.36 % 

💻 Operating System: 
WSL                      17 hrs 45 mins      █████████████████████░░░░   85.35 % 
Mac                      3 hrs 2 mins        ████░░░░░░░░░░░░░░░░░░░░░   14.65 % 
```

🤖 **AI Coding This Week** 

```text
⏱ AI Coding Time: 19 hrs 17 mins (92.68%)

✍️ 5,362 lines written by AI, 301 lines written by hand (94.68% AI-written)

🔤 502,825,838 Input Tokens, 1,375,575 Output Tokens

💵 $2016.85 Estimated AI Cost This Week

🧠 54 AI Sessions, 625 AI Prompts

GPT                      5,414 lines         █████████████████████████   100.00 % 

🔎 AI Coding Insights:
🤖 AI-Driven — 94.68% of written lines came from AI
📚 Verbose Prompter — average 7,255 characters per prompt
🔁 Iterative Prompter — average 12 prompts per session
🚀 High AI Trust — 12.61% of changed lines were hand-edited
```

**I Mostly Code in Ruby** 

```text
Ruby                     8 repos             █████████████░░░░░░░░░░░░   53.33 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   13.33 % 
Java                     1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
Shell                    1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
CSS                      1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
```




 Last Updated on 02/08/2026 18:48:11 UTC
<!--END_SECTION:waka-->
