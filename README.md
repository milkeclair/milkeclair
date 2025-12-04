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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C750%20hrs%2056%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-338.4%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                799 commits         █████░░░░░░░░░░░░░░░░░░░░   20.49 % 
🌆 Daytime                899 commits         ██████░░░░░░░░░░░░░░░░░░░   23.05 % 
🌃 Evening                1171 commits        ████████░░░░░░░░░░░░░░░░░   30.03 % 
🌙 Night                  1031 commits        ███████░░░░░░░░░░░░░░░░░░   26.44 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   505 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.95 % 
Tuesday                  554 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.21 % 
Wednesday                447 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.46 % 
Thursday                 540 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.85 % 
Friday                   695 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.82 % 
Saturday                 385 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.87 % 
Sunday                   774 commits         █████░░░░░░░░░░░░░░░░░░░░   19.85 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     25 hrs 48 mins      ███████████░░░░░░░░░░░░░░   43.94 % 
TypeScript               16 hrs 20 mins      ███████░░░░░░░░░░░░░░░░░░   27.82 % 
Markdown                 8 hrs 12 mins       ███░░░░░░░░░░░░░░░░░░░░░░   13.98 % 
Ruby                     4 hrs 46 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   08.12 % 
Other                    1 hr 50 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   03.14 % 

💻 Operating System: 
WSL                      46 hrs 40 mins      ████████████████████░░░░░   79.46 % 
Mac                      12 hrs 3 mins       █████░░░░░░░░░░░░░░░░░░░░   20.54 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            █████████████░░░░░░░░░░░░   52.63 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   21.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 04/12/2025 18:45:08 UTC
<!--END_SECTION:waka-->
