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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C059%20hrs%2037%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-439.21%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1054 commits        ██████░░░░░░░░░░░░░░░░░░░   22.18 % 
🌆 Daytime                1079 commits        ██████░░░░░░░░░░░░░░░░░░░   22.71 % 
🌃 Evening                1438 commits        ████████░░░░░░░░░░░░░░░░░   30.27 % 
🌙 Night                  1180 commits        ██████░░░░░░░░░░░░░░░░░░░   24.84 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   695 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.63 % 
Tuesday                  677 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.25 % 
Wednesday                513 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.80 % 
Thursday                 616 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.97 % 
Friday                   810 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.05 % 
Saturday                 501 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.55 % 
Sunday                   939 commits         █████░░░░░░░░░░░░░░░░░░░░   19.76 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Markdown                 6 hrs 33 mins       ██████████░░░░░░░░░░░░░░░   38.44 % 
Ruby                     5 hrs 4 mins        ███████░░░░░░░░░░░░░░░░░░   29.76 % 
Bash                     4 hrs 25 mins       ██████░░░░░░░░░░░░░░░░░░░   25.95 % 
TypeScript               16 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.64 % 
Other                    16 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.64 % 

💻 Operating System: 
WSL                      16 hrs 54 mins      █████████████████████████   99.16 % 
Mac                      8 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.84 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   50.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 22/02/2026 18:45:13 UTC
<!--END_SECTION:waka-->
