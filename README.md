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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C381%20hrs%2041%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-488.61%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1089 commits        █████░░░░░░░░░░░░░░░░░░░░   21.27 % 
🌆 Daytime                1207 commits        ██████░░░░░░░░░░░░░░░░░░░   23.57 % 
🌃 Evening                1554 commits        ████████░░░░░░░░░░░░░░░░░   30.35 % 
🌙 Night                  1271 commits        ██████░░░░░░░░░░░░░░░░░░░   24.82 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   711 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.88 % 
Tuesday                  727 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.20 % 
Wednesday                534 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.43 % 
Thursday                 661 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.91 % 
Friday                   872 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.03 % 
Saturday                 581 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.35 % 
Sunday                   1035 commits        █████░░░░░░░░░░░░░░░░░░░░   20.21 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Other                    12 hrs 35 mins      ███████████░░░░░░░░░░░░░░   45.22 % 
Ruby                     8 hrs 49 mins       ████████░░░░░░░░░░░░░░░░░   31.65 % 
Markdown                 2 hrs 2 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   07.36 % 
TypeScript               1 hr 12 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   04.33 % 
Bash                     50 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   03.00 % 

💻 Operating System: 
WSL                      27 hrs 19 mins      █████████████████████████   98.05 % 
Windows                  32 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.95 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 10/05/2026 18:47:29 UTC
<!--END_SECTION:waka-->
