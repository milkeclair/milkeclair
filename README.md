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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C790%20hrs%2024%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-341.7%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                801 commits         █████░░░░░░░░░░░░░░░░░░░░   20.48 % 
🌆 Daytime                902 commits         ██████░░░░░░░░░░░░░░░░░░░   23.06 % 
🌃 Evening                1171 commits        ███████░░░░░░░░░░░░░░░░░░   29.94 % 
🌙 Night                  1037 commits        ███████░░░░░░░░░░░░░░░░░░   26.51 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   509 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.01 % 
Tuesday                  556 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.22 % 
Wednesday                450 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.51 % 
Thursday                 540 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.81 % 
Friday                   697 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.82 % 
Saturday                 385 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.84 % 
Sunday                   774 commits         █████░░░░░░░░░░░░░░░░░░░░   19.79 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
TypeScript               33 hrs 41 mins      █████████████████░░░░░░░░   69.62 % 
Ruby                     8 hrs 10 mins       ████░░░░░░░░░░░░░░░░░░░░░   16.89 % 
Markdown                 4 hrs 1 min         ██░░░░░░░░░░░░░░░░░░░░░░░   08.32 % 
JSON                     48 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.67 % 
Other                    39 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.36 % 

💻 Operating System: 
WSL                      35 hrs 21 mins      ██████████████████░░░░░░░   73.06 % 
Mac                      13 hrs 2 mins       ███████░░░░░░░░░░░░░░░░░░   26.94 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   50.00 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   20.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
TypeScript               1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 11/12/2025 18:44:25 UTC
<!--END_SECTION:waka-->
