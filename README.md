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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C526%20hrs%208%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-605.98%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1370 commits        █████░░░░░░░░░░░░░░░░░░░░   21.12 % 
🌆 Daytime                1554 commits        ██████░░░░░░░░░░░░░░░░░░░   23.95 % 
🌃 Evening                1885 commits        ███████░░░░░░░░░░░░░░░░░░   29.05 % 
🌙 Night                  1679 commits        ██████░░░░░░░░░░░░░░░░░░░   25.88 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   831 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.81 % 
Tuesday                  899 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.86 % 
Wednesday                641 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.88 % 
Thursday                 814 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.55 % 
Friday                   1198 commits        █████░░░░░░░░░░░░░░░░░░░░   18.46 % 
Saturday                 729 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.24 % 
Sunday                   1376 commits        █████░░░░░░░░░░░░░░░░░░░░   21.21 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Java                     27 hrs 1 min        ██████████████████░░░░░░░   72.39 % 
Markdown                 4 hrs 18 mins       ███░░░░░░░░░░░░░░░░░░░░░░   11.56 % 
Ruby                     2 hrs 4 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   05.55 % 
Other                    1 hr 46 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
Bash                     46 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.07 % 

💻 Operating System: 
WSL                      33 hrs 49 mins      ███████████████████████░░   90.59 % 
Mac                      2 hrs 39 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   07.13 % 
Windows                  51 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.28 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Shell                    2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Java                     1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 08/06/2026 19:17:57 UTC
<!--END_SECTION:waka-->
