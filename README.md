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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C037%20hrs%2044%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-397.85%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                958 commits         █████░░░░░░░░░░░░░░░░░░░░   21.18 % 
🌆 Daytime                1056 commits        ██████░░░░░░░░░░░░░░░░░░░   23.35 % 
🌃 Evening                1370 commits        ████████░░░░░░░░░░░░░░░░░   30.29 % 
🌙 Night                  1139 commits        ██████░░░░░░░░░░░░░░░░░░░   25.18 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   643 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.22 % 
Tuesday                  651 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.39 % 
Wednesday                504 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.14 % 
Thursday                 600 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.27 % 
Friday                   774 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.11 % 
Saturday                 470 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.39 % 
Sunday                   881 commits         █████░░░░░░░░░░░░░░░░░░░░   19.48 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     9 hrs 12 mins       ████████████░░░░░░░░░░░░░   47.43 % 
Markdown                 4 hrs 20 mins       ██████░░░░░░░░░░░░░░░░░░░   22.39 % 
tmux                     2 hrs 17 mins       ███░░░░░░░░░░░░░░░░░░░░░░   11.78 % 
Bash                     1 hr 40 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   08.66 % 
JSON                     42 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   03.61 % 

💻 Operating System: 
WSL                      19 hrs 5 mins       █████████████████████████   98.27 % 
Mac                      20 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.73 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   50.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 13/02/2026 18:46:23 UTC
<!--END_SECTION:waka-->
