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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C550%20hrs%2033%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-610.79%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1370 commits        █████░░░░░░░░░░░░░░░░░░░░   21.09 % 
🌆 Daytime                1554 commits        ██████░░░░░░░░░░░░░░░░░░░   23.92 % 
🌃 Evening                1885 commits        ███████░░░░░░░░░░░░░░░░░░   29.02 % 
🌙 Night                  1687 commits        ██████░░░░░░░░░░░░░░░░░░░   25.97 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   831 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.79 % 
Tuesday                  899 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.84 % 
Wednesday                641 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.87 % 
Thursday                 816 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.56 % 
Friday                   1204 commits        █████░░░░░░░░░░░░░░░░░░░░   18.53 % 
Saturday                 729 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.22 % 
Sunday                   1376 commits        █████░░░░░░░░░░░░░░░░░░░░   21.18 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Java                     18 hrs 18 mins      ████████████░░░░░░░░░░░░░   46.50 % 
Python                   8 hrs 27 mins       █████░░░░░░░░░░░░░░░░░░░░   21.47 % 
Markdown                 5 hrs 22 mins       ███░░░░░░░░░░░░░░░░░░░░░░   13.63 % 
Other                    2 hrs 25 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   06.15 % 
Ruby                     2 hrs 3 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   05.25 % 

💻 Operating System: 
WSL                      35 hrs 16 mins      ██████████████████████░░░   89.56 % 
Mac                      3 hrs 15 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   08.28 % 
Windows                  51 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.16 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Shell                    2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Java                     1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 11/06/2026 19:24:34 UTC
<!--END_SECTION:waka-->
