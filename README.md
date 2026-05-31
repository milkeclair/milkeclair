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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C476%20hrs%206%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-610.52%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1373 commits        █████░░░░░░░░░░░░░░░░░░░░   21.09 % 
🌆 Daytime                1560 commits        ██████░░░░░░░░░░░░░░░░░░░   23.97 % 
🌃 Evening                1899 commits        ███████░░░░░░░░░░░░░░░░░░   29.17 % 
🌙 Night                  1677 commits        ██████░░░░░░░░░░░░░░░░░░░   25.76 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   830 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.75 % 
Tuesday                  898 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.80 % 
Wednesday                651 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
Thursday                 812 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.48 % 
Friday                   1202 commits        █████░░░░░░░░░░░░░░░░░░░░   18.47 % 
Saturday                 733 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.26 % 
Sunday                   1383 commits        █████░░░░░░░░░░░░░░░░░░░░   21.25 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Markdown                 9 hrs 59 mins       ████████████░░░░░░░░░░░░░   47.39 % 
Other                    2 hrs 55 mins       ███░░░░░░░░░░░░░░░░░░░░░░   13.89 % 
Ruby                     2 hrs 21 mins       ███░░░░░░░░░░░░░░░░░░░░░░   11.19 % 
PowerShell               1 hr 53 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   09.00 % 
Batchfile                1 hr 17 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   06.16 % 

💻 Operating System: 
Mac                      12 hrs 16 mins      ███████████████░░░░░░░░░░   58.24 % 
WSL                      6 hrs 4 mins        ███████░░░░░░░░░░░░░░░░░░   28.80 % 
Windows                  2 hrs 43 mins       ███░░░░░░░░░░░░░░░░░░░░░░   12.96 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ███████████░░░░░░░░░░░░░░   45.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
Batchfile                2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 31/05/2026 18:52:52 UTC
<!--END_SECTION:waka-->
