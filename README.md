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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C700%20hrs%2026%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-327.6%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                777 commits         █████░░░░░░░░░░░░░░░░░░░░   20.26 % 
🌆 Daytime                899 commits         ██████░░░░░░░░░░░░░░░░░░░   23.44 % 
🌃 Evening                1136 commits        ███████░░░░░░░░░░░░░░░░░░   29.62 % 
🌙 Night                  1023 commits        ███████░░░░░░░░░░░░░░░░░░   26.68 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   491 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.80 % 
Tuesday                  551 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.37 % 
Wednesday                446 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.63 % 
Thursday                 540 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.08 % 
Friday                   695 commits         █████░░░░░░░░░░░░░░░░░░░░   18.12 % 
Saturday                 363 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.47 % 
Sunday                   749 commits         █████░░░░░░░░░░░░░░░░░░░░   19.53 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     17 hrs 46 mins      ██████████░░░░░░░░░░░░░░░   39.14 % 
Ruby                     16 hrs 26 mins      █████████░░░░░░░░░░░░░░░░   36.21 % 
Markdown                 4 hrs 52 mins       ███░░░░░░░░░░░░░░░░░░░░░░   10.75 % 
Other                    3 hrs 3 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   06.73 % 
TypeScript               2 hrs 39 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.84 % 

💻 Operating System: 
WSL                      39 hrs 54 mins      ██████████████████████░░░   87.91 % 
Mac                      5 hrs 29 mins       ███░░░░░░░░░░░░░░░░░░░░░░   12.09 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            █████████████░░░░░░░░░░░░   52.63 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   21.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 28/11/2025 18:41:11 UTC
<!--END_SECTION:waka-->
