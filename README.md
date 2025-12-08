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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C783%20hrs%2019%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-341.5%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                801 commits         █████░░░░░░░░░░░░░░░░░░░░   20.50 % 
🌆 Daytime                899 commits         ██████░░░░░░░░░░░░░░░░░░░   23.00 % 
🌃 Evening                1171 commits        ███████░░░░░░░░░░░░░░░░░░   29.96 % 
🌙 Night                  1037 commits        ███████░░░░░░░░░░░░░░░░░░   26.54 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   509 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.02 % 
Tuesday                  556 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.23 % 
Wednesday                447 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.44 % 
Thursday                 540 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.82 % 
Friday                   697 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.84 % 
Saturday                 385 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.85 % 
Sunday                   774 commits         █████░░░░░░░░░░░░░░░░░░░░   19.81 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
TypeScript               38 hrs 16 mins      ████████████████░░░░░░░░░   62.54 % 
Bash                     10 hrs 7 mins       ████░░░░░░░░░░░░░░░░░░░░░   16.56 % 
Markdown                 4 hrs 58 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   08.12 % 
Ruby                     4 hrs 9 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   06.78 % 
JSON                     1 hr 9 mins         ░░░░░░░░░░░░░░░░░░░░░░░░░   01.89 % 

💻 Operating System: 
WSL                      51 hrs 42 mins      █████████████████████░░░░   84.49 % 
Mac                      9 hrs 29 mins       ████░░░░░░░░░░░░░░░░░░░░░   15.51 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   50.00 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   20.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
TypeScript               1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 08/12/2025 18:44:17 UTC
<!--END_SECTION:waka-->
