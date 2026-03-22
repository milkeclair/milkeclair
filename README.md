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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C174%20hrs%2036%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-433.45%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                982 commits         █████░░░░░░░░░░░░░░░░░░░░   20.69 % 
🌆 Daytime                1133 commits        ██████░░░░░░░░░░░░░░░░░░░   23.87 % 
🌃 Evening                1441 commits        ████████░░░░░░░░░░░░░░░░░   30.36 % 
🌙 Night                  1190 commits        ██████░░░░░░░░░░░░░░░░░░░   25.07 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   652 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.74 % 
Tuesday                  685 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.43 % 
Wednesday                514 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.83 % 
Thursday                 623 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.13 % 
Friday                   814 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.15 % 
Saturday                 514 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.83 % 
Sunday                   944 commits         █████░░░░░░░░░░░░░░░░░░░░   19.89 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     12 hrs 53 mins      ███████████████████░░░░░░   74.29 % 
TypeScript               2 hrs 1 min         ███░░░░░░░░░░░░░░░░░░░░░░   11.68 % 
Markdown                 1 hr 19 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   07.62 % 
Other                    21 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.11 % 
Bash                     19 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.84 % 

💻 Operating System: 
WSL                      14 hrs 14 mins      █████████████████████░░░░   82.12 % 
Mac                      3 hrs 6 mins        ████░░░░░░░░░░░░░░░░░░░░░   17.88 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 22/03/2026 18:44:43 UTC
<!--END_SECTION:waka-->
