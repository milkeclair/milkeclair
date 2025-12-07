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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C774%20hrs%2012%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-338.8%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                801 commits         █████░░░░░░░░░░░░░░░░░░░░   20.53 % 
🌆 Daytime                899 commits         ██████░░░░░░░░░░░░░░░░░░░   23.04 % 
🌃 Evening                1171 commits        ████████░░░░░░░░░░░░░░░░░   30.01 % 
🌙 Night                  1031 commits        ███████░░░░░░░░░░░░░░░░░░   26.42 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   505 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.94 % 
Tuesday                  554 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.20 % 
Wednesday                447 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.46 % 
Thursday                 540 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.84 % 
Friday                   697 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.86 % 
Saturday                 385 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.87 % 
Sunday                   774 commits         █████░░░░░░░░░░░░░░░░░░░░   19.84 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
TypeScript               33 hrs 11 mins      ██████████████░░░░░░░░░░░   54.89 % 
Bash                     14 hrs 46 mins      ██████░░░░░░░░░░░░░░░░░░░   24.42 % 
Markdown                 5 hrs 3 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   08.37 % 
Ruby                     3 hrs 52 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   06.40 % 
JSON                     1 hr 4 mins         ░░░░░░░░░░░░░░░░░░░░░░░░░   01.77 % 

💻 Operating System: 
WSL                      50 hrs 59 mins      █████████████████████░░░░   84.31 % 
Mac                      9 hrs 29 mins       ████░░░░░░░░░░░░░░░░░░░░░   15.69 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   50.00 % 
Shell                    4 repos             █████░░░░░░░░░░░░░░░░░░░░   20.00 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   20.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 07/12/2025 18:40:24 UTC
<!--END_SECTION:waka-->
