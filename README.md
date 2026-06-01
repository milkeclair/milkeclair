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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C489%20hrs%2015%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-610.88%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1373 commits        █████░░░░░░░░░░░░░░░░░░░░   21.08 % 
🌆 Daytime                1560 commits        ██████░░░░░░░░░░░░░░░░░░░   23.96 % 
🌃 Evening                1900 commits        ███████░░░░░░░░░░░░░░░░░░   29.18 % 
🌙 Night                  1679 commits        ██████░░░░░░░░░░░░░░░░░░░   25.78 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   831 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.76 % 
Tuesday                  900 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.82 % 
Wednesday                651 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
Thursday                 812 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.47 % 
Friday                   1202 commits        █████░░░░░░░░░░░░░░░░░░░░   18.46 % 
Saturday                 733 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.26 % 
Sunday                   1383 commits        █████░░░░░░░░░░░░░░░░░░░░   21.24 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Markdown                 10 hrs 2 mins       █████████░░░░░░░░░░░░░░░░   36.36 % 
Kotlin                   3 hrs 16 mins       ███░░░░░░░░░░░░░░░░░░░░░░   11.87 % 
Other                    2 hrs 56 mins       ███░░░░░░░░░░░░░░░░░░░░░░   10.68 % 
Ruby                     2 hrs 21 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   08.54 % 
Batchfile                1 hr 55 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   06.97 % 

💻 Operating System: 
WSL                      12 hrs 36 mins      ███████████░░░░░░░░░░░░░░   45.67 % 
Mac                      12 hrs 16 mins      ███████████░░░░░░░░░░░░░░   44.44 % 
Windows                  2 hrs 43 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   09.89 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ███████████░░░░░░░░░░░░░░   45.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
Java                     1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 01/06/2026 20:02:04 UTC
<!--END_SECTION:waka-->
