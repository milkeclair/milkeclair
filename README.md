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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C497%20hrs%2050%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-600.95%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1368 commits        █████░░░░░░░░░░░░░░░░░░░░   21.12 % 
🌆 Daytime                1554 commits        ██████░░░░░░░░░░░░░░░░░░░   23.99 % 
🌃 Evening                1883 commits        ███████░░░░░░░░░░░░░░░░░░   29.07 % 
🌙 Night                  1673 commits        ██████░░░░░░░░░░░░░░░░░░░   25.83 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   828 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.78 % 
Tuesday                  896 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.83 % 
Wednesday                641 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.90 % 
Thursday                 810 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.50 % 
Friday                   1198 commits        █████░░░░░░░░░░░░░░░░░░░░   18.49 % 
Saturday                 729 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.25 % 
Sunday                   1376 commits        █████░░░░░░░░░░░░░░░░░░░░   21.24 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Markdown                 6 hrs 37 mins       ███████░░░░░░░░░░░░░░░░░░   26.62 % 
Kotlin                   3 hrs 53 mins       ████░░░░░░░░░░░░░░░░░░░░░   15.61 % 
Java                     3 hrs 49 mins       ████░░░░░░░░░░░░░░░░░░░░░   15.39 % 
Other                    2 hrs 11 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   08.78 % 
Batchfile                1 hr 55 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   07.74 % 

💻 Operating System: 
WSL                      16 hrs 17 mins      ████████████████░░░░░░░░░   65.50 % 
Mac                      6 hrs 33 mins       ███████░░░░░░░░░░░░░░░░░░   26.34 % 
Windows                  2 hrs 1 min         ██░░░░░░░░░░░░░░░░░░░░░░░   08.16 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Shell                    2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Java                     1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 02/06/2026 19:45:36 UTC
<!--END_SECTION:waka-->
