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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C059%20hrs%2055%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-439.22%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1054 commits        ██████░░░░░░░░░░░░░░░░░░░   22.18 % 
🌆 Daytime                1080 commits        ██████░░░░░░░░░░░░░░░░░░░   22.73 % 
🌃 Evening                1438 commits        ████████░░░░░░░░░░░░░░░░░   30.26 % 
🌙 Night                  1180 commits        ██████░░░░░░░░░░░░░░░░░░░   24.83 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   696 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.65 % 
Tuesday                  677 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.25 % 
Wednesday                513 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.80 % 
Thursday                 616 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.96 % 
Friday                   810 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.05 % 
Saturday                 501 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.54 % 
Sunday                   939 commits         █████░░░░░░░░░░░░░░░░░░░░   19.76 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     4 hrs 43 mins       ████████░░░░░░░░░░░░░░░░░   32.51 % 
Markdown                 4 hrs 32 mins       ████████░░░░░░░░░░░░░░░░░   31.32 % 
Ruby                     4 hrs 16 mins       ███████░░░░░░░░░░░░░░░░░░   29.48 % 
TypeScript               16 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.93 % 
Other                    15 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.82 % 

💻 Operating System: 
WSL                      14 hrs 22 mins      █████████████████████████   99.02 % 
Mac                      8 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.98 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   50.00 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.00 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   10.00 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.00 % 
```




 Last Updated on 23/02/2026 18:48:20 UTC
<!--END_SECTION:waka-->
