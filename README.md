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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C719%20hrs%2032%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-338.4%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                799 commits         █████░░░░░░░░░░░░░░░░░░░░   20.49 % 
🌆 Daytime                899 commits         ██████░░░░░░░░░░░░░░░░░░░   23.06 % 
🌃 Evening                1171 commits        ████████░░░░░░░░░░░░░░░░░   30.03 % 
🌙 Night                  1030 commits        ███████░░░░░░░░░░░░░░░░░░   26.42 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   505 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.95 % 
Tuesday                  554 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.21 % 
Wednesday                446 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.44 % 
Thursday                 540 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.85 % 
Friday                   695 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.83 % 
Saturday                 385 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.87 % 
Sunday                   774 commits         █████░░░░░░░░░░░░░░░░░░░░   19.85 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     26 hrs 43 mins      █████████████░░░░░░░░░░░░   51.98 % 
Ruby                     13 hrs 10 mins      ██████░░░░░░░░░░░░░░░░░░░   25.63 % 
Markdown                 4 hrs 51 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   09.44 % 
TypeScript               4 hrs 33 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   08.85 % 
Other                    1 hr 41 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   03.28 % 

💻 Operating System: 
WSL                      46 hrs              ██████████████████████░░░   89.46 % 
Mac                      5 hrs 25 mins       ███░░░░░░░░░░░░░░░░░░░░░░   10.54 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            █████████████░░░░░░░░░░░░   52.63 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   21.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 02/12/2025 18:44:50 UTC
<!--END_SECTION:waka-->
