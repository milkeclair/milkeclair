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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C661%20hrs%2014%20mins-blue?style=flat)

![AI Code Time](http://img.shields.io/badge/AI%20Code%20Time-401%20hrs%2056%20mins-blue?style=flat)

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
Markdown                 19 hrs 40 mins      ██████████████████░░░░░░░   73.63 % 
Other                    3 hrs 45 mins       ████░░░░░░░░░░░░░░░░░░░░░   14.06 % 
Python                   56 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   03.52 % 
INI                      43 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.73 % 
PowerShell               33 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.12 % 

💻 Operating System: 
WSL                      23 hrs 40 mins      ██████████████████████░░░   88.60 % 
Mac                      3 hrs 2 mins        ███░░░░░░░░░░░░░░░░░░░░░░   11.40 % 
```

🤖 **AI Coding This Week** 

```text
⏱ AI Coding Time: 24 hrs 54 mins (93.19%)

✍️ 4,928 lines written by AI, 303 lines written by hand (94.21% AI-written)

🔤 648,806,410 Input Tokens, 1,845,928 Output Tokens

💵 $2525.80 Estimated AI Cost This Week

🧠 66 AI Sessions, 737 AI Prompts

GPT                      4,973 lines         █████████████████████████   100.00 % 

🔎 AI Coding Insights:
🤖 AI-Driven — 94.21% of written lines came from AI
📚 Verbose Prompter — average 7,607 characters per prompt
🔁 Iterative Prompter — average 11 prompts per session
🚀 High AI Trust — 13.62% of changed lines were hand-edited
```

**I Mostly Code in Ruby** 

```text
Ruby                     8 repos             █████████████░░░░░░░░░░░░   53.33 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   13.33 % 
Java                     1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
Shell                    1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
CSS                      1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
```




 Last Updated on 30/07/2026 18:58:55 UTC
<!--END_SECTION:waka-->
