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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C543%20hrs%2018%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-607.06%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1370 commits        █████░░░░░░░░░░░░░░░░░░░░   21.11 % 
🌆 Daytime                1554 commits        ██████░░░░░░░░░░░░░░░░░░░   23.94 % 
🌃 Evening                1885 commits        ███████░░░░░░░░░░░░░░░░░░   29.04 % 
🌙 Night                  1681 commits        ██████░░░░░░░░░░░░░░░░░░░   25.90 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   831 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.80 % 
Tuesday                  899 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.85 % 
Wednesday                641 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.88 % 
Thursday                 816 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.57 % 
Friday                   1198 commits        █████░░░░░░░░░░░░░░░░░░░░   18.46 % 
Saturday                 729 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.23 % 
Sunday                   1376 commits        █████░░░░░░░░░░░░░░░░░░░░   21.20 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Java                     15 hrs 22 mins      ███████████░░░░░░░░░░░░░░   42.11 % 
Python                   8 hrs 27 mins       ██████░░░░░░░░░░░░░░░░░░░   23.17 % 
Markdown                 5 hrs 36 mins       ████░░░░░░░░░░░░░░░░░░░░░   15.39 % 
Other                    2 hrs 21 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   06.44 % 
Ruby                     2 hrs 4 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   05.68 % 

💻 Operating System: 
WSL                      32 hrs 22 mins      ██████████████████████░░░   88.70 % 
Mac                      3 hrs 16 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   08.96 % 
Windows                  51 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.33 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Shell                    2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Java                     1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 10/06/2026 19:23:11 UTC
<!--END_SECTION:waka-->
