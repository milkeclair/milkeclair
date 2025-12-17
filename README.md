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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C829%20hrs%2037%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-380.0%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                905 commits         █████░░░░░░░░░░░░░░░░░░░░   21.71 % 
🌆 Daytime                938 commits         ██████░░░░░░░░░░░░░░░░░░░   22.50 % 
🌃 Evening                1251 commits        ████████░░░░░░░░░░░░░░░░░   30.01 % 
🌙 Night                  1075 commits        ██████░░░░░░░░░░░░░░░░░░░   25.79 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   561 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.46 % 
Tuesday                  589 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.13 % 
Wednesday                474 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.37 % 
Thursday                 556 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.34 % 
Friday                   743 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.82 % 
Saturday                 420 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.07 % 
Sunday                   826 commits         █████░░░░░░░░░░░░░░░░░░░░   19.81 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     21 hrs 20 mins      ██████████████░░░░░░░░░░░   54.40 % 
TypeScript               8 hrs 53 mins       ██████░░░░░░░░░░░░░░░░░░░   22.66 % 
Markdown                 2 hrs 37 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   06.69 % 
Other                    2 hrs 18 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.87 % 
Bash                     1 hr 59 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   05.08 % 

💻 Operating System: 
WSL                      30 hrs 57 mins      ████████████████████░░░░░   78.92 % 
Mac                      8 hrs 16 mins       █████░░░░░░░░░░░░░░░░░░░░   21.08 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   47.62 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   19.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   14.29 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   09.52 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
```




 Last Updated on 17/12/2025 18:45:02 UTC
<!--END_SECTION:waka-->
