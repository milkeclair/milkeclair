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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C615%20hrs%2023%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-536.95%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1266 commits        █████░░░░░░░░░░░░░░░░░░░░   20.84 % 
🌆 Daytime                1456 commits        ██████░░░░░░░░░░░░░░░░░░░   23.97 % 
🌃 Evening                1710 commits        ███████░░░░░░░░░░░░░░░░░░   28.15 % 
🌙 Night                  1642 commits        ███████░░░░░░░░░░░░░░░░░░   27.03 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   745 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.27 % 
Tuesday                  842 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.86 % 
Wednesday                607 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.99 % 
Thursday                 762 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.55 % 
Friday                   1153 commits        █████░░░░░░░░░░░░░░░░░░░░   18.98 % 
Saturday                 676 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.13 % 
Sunday                   1289 commits        █████░░░░░░░░░░░░░░░░░░░░   21.22 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     12 hrs 8 mins       █████████████░░░░░░░░░░░░   52.38 % 
Markdown                 6 hrs 45 mins       ███████░░░░░░░░░░░░░░░░░░   29.16 % 
Ruby                     3 hrs 13 mins       ███░░░░░░░░░░░░░░░░░░░░░░   13.94 % 
Python                   23 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.67 % 
TypeScript               14 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.06 % 

💻 Operating System: 
WSL                      21 hrs 26 mins      ███████████████████████░░   92.43 % 
Mac                      1 hr 40 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   07.20 % 
Windows                  5 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.37 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     8 repos             █████████████░░░░░░░░░░░░   53.33 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   13.33 % 
Java                     1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
Shell                    1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
CSS                      1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
```




 Last Updated on 01/07/2026 19:10:09 UTC
<!--END_SECTION:waka-->
