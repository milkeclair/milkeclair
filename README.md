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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C802%20hrs%2027%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-378.3%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                898 commits         █████░░░░░░░░░░░░░░░░░░░░   21.66 % 
🌆 Daytime                928 commits         ██████░░░░░░░░░░░░░░░░░░░   22.39 % 
🌃 Evening                1244 commits        ████████░░░░░░░░░░░░░░░░░   30.01 % 
🌙 Night                  1075 commits        ██████░░░░░░░░░░░░░░░░░░░   25.93 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   561 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.53 % 
Tuesday                  580 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.99 % 
Wednesday                459 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.07 % 
Thursday                 556 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.41 % 
Friday                   743 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.93 % 
Saturday                 420 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.13 % 
Sunday                   826 commits         █████░░░░░░░░░░░░░░░░░░░░   19.93 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
TypeScript               23 hrs 28 mins      ███████████████░░░░░░░░░░   59.29 % 
Ruby                     8 hrs 54 mins       ██████░░░░░░░░░░░░░░░░░░░   22.48 % 
Markdown                 4 hrs 29 mins       ███░░░░░░░░░░░░░░░░░░░░░░   11.34 % 
Bash                     1 hr 22 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   03.48 % 
JSON                     45 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.91 % 

💻 Operating System: 
WSL                      32 hrs 46 mins      █████████████████████░░░░   82.78 % 
Mac                      6 hrs 49 mins       ████░░░░░░░░░░░░░░░░░░░░░   17.22 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   47.62 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   19.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   14.29 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   09.52 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
```




 Last Updated on 13/12/2025 18:40:30 UTC
<!--END_SECTION:waka-->
