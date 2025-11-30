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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C710%20hrs%2052%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-358.8%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                870 commits         █████░░░░░░░░░░░░░░░░░░░░   21.35 % 
🌆 Daytime                914 commits         ██████░░░░░░░░░░░░░░░░░░░   22.43 % 
🌃 Evening                1229 commits        ████████░░░░░░░░░░░░░░░░░   30.17 % 
🌙 Night                  1061 commits        ███████░░░░░░░░░░░░░░░░░░   26.04 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   530 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.01 % 
Tuesday                  574 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.09 % 
Wednesday                455 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.17 % 
Thursday                 556 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.65 % 
Friday                   731 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.94 % 
Saturday                 410 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.06 % 
Sunday                   818 commits         █████░░░░░░░░░░░░░░░░░░░░   20.08 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     26 hrs 33 mins      █████████████░░░░░░░░░░░░   53.24 % 
Ruby                     12 hrs 7 mins       ██████░░░░░░░░░░░░░░░░░░░   24.31 % 
Markdown                 4 hrs 59 mins       ███░░░░░░░░░░░░░░░░░░░░░░   10.01 % 
Other                    3 hrs 5 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   06.19 % 
TypeScript               2 hrs 39 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.31 % 

💻 Operating System: 
WSL                      44 hrs 24 mins      ██████████████████████░░░   89.00 % 
Mac                      5 hrs 29 mins       ███░░░░░░░░░░░░░░░░░░░░░░   11.00 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            █████████████░░░░░░░░░░░░   52.63 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   21.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 30/11/2025 18:41:08 UTC
<!--END_SECTION:waka-->
