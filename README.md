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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C610%20hrs%2017%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-596.41%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1388 commits        █████░░░░░░░░░░░░░░░░░░░░   21.56 % 
🌆 Daytime                1528 commits        ██████░░░░░░░░░░░░░░░░░░░   23.73 % 
🌃 Evening                1808 commits        ███████░░░░░░░░░░░░░░░░░░   28.08 % 
🌙 Night                  1715 commits        ███████░░░░░░░░░░░░░░░░░░   26.63 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   799 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.41 % 
Tuesday                  882 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.70 % 
Wednesday                615 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.55 % 
Thursday                 811 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.60 % 
Friday                   1244 commits        █████░░░░░░░░░░░░░░░░░░░░   19.32 % 
Saturday                 718 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.15 % 
Sunday                   1370 commits        █████░░░░░░░░░░░░░░░░░░░░   21.28 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     9 hrs 47 mins       ███████████░░░░░░░░░░░░░░   44.11 % 
Markdown                 7 hrs 9 mins        ████████░░░░░░░░░░░░░░░░░   32.26 % 
Ruby                     3 hrs 33 mins       ████░░░░░░░░░░░░░░░░░░░░░   16.04 % 
TypeScript               49 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   03.70 % 
Python                   23 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.74 % 

💻 Operating System: 
WSL                      20 hrs 27 mins      ███████████████████████░░   92.09 % 
Mac                      1 hr 40 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   07.52 % 
Windows                  5 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.39 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     8 repos             █████████████░░░░░░░░░░░░   53.33 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   13.33 % 
Java                     1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
Shell                    1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
CSS                      1 repo              ██░░░░░░░░░░░░░░░░░░░░░░░   06.67 % 
```




 Last Updated on 29/06/2026 19:12:47 UTC
<!--END_SECTION:waka-->
