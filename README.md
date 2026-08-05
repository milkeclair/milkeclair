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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C667%20hrs%2010%20mins-blue?style=flat)

![AI Code Time](http://img.shields.io/badge/AI%20Code%20Time-408%20hrs%2040%20mins-blue?style=flat)

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
Markdown                 7 hrs 34 mins       █████████████░░░░░░░░░░░░   50.94 % 
Other                    2 hrs 58 mins       █████░░░░░░░░░░░░░░░░░░░░   20.02 % 
JavaScript               1 hr 44 mins        ███░░░░░░░░░░░░░░░░░░░░░░   11.69 % 
JSON                     1 hr 19 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   08.93 % 
Ruby                     49 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   05.54 % 

💻 Operating System: 
WSL                      14 hrs 46 mins      █████████████████████████   99.54 % 
Mac                      4 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.46 % 
```

🤖 **AI Coding This Week** 

```text
⏱ AI Coding Time: 12 hrs 42 mins (85.64%)

✍️ 3,780 lines written by AI, 12 lines written by hand (99.68% AI-written)

🔤 406,534,829 Input Tokens, 921,050 Output Tokens

💵 $1079.86 Estimated AI Cost This Week

🧠 48 AI Sessions, 817 AI Prompts

GPT                      3,812 lines         █████████████████████████   100.00 % 

🔎 AI Coding Insights:
🤖 AI-Driven — 99.68% of written lines came from AI
📚 Verbose Prompter — average 6,235 characters per prompt
🔁 Iterative Prompter — average 17 prompts per session
🚀 High AI Trust — 5.41% of changed lines were hand-edited
```

**I Mostly Code in Ruby** 

```text
Ruby                     8 repos             █████████████░░░░░░░░░░░░   53.33 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   13.33 % 
Java                     1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
Shell                    1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
CSS                      1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
```




 Last Updated on 05/08/2026 19:02:11 UTC
<!--END_SECTION:waka-->
