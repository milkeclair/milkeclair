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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C362%20hrs%2026%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-486.34%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1089 commits        █████░░░░░░░░░░░░░░░░░░░░   21.37 % 
🌆 Daytime                1195 commits        ██████░░░░░░░░░░░░░░░░░░░   23.45 % 
🌃 Evening                1547 commits        ████████░░░░░░░░░░░░░░░░░   30.36 % 
🌙 Night                  1265 commits        ██████░░░░░░░░░░░░░░░░░░░   24.82 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   708 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.89 % 
Tuesday                  727 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.27 % 
Wednesday                534 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.48 % 
Thursday                 661 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.97 % 
Friday                   872 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.11 % 
Saturday                 569 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.17 % 
Sunday                   1025 commits        █████░░░░░░░░░░░░░░░░░░░░   20.11 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Other                    5 hrs 51 mins       ██████████████░░░░░░░░░░░   55.34 % 
Markdown                 1 hr 26 mins        ███░░░░░░░░░░░░░░░░░░░░░░   13.55 % 
TypeScript               1 hr 12 mins        ███░░░░░░░░░░░░░░░░░░░░░░   11.39 % 
JSON                     49 mins             ██░░░░░░░░░░░░░░░░░░░░░░░   07.77 % 
Bash                     36 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   05.71 % 

💻 Operating System: 
WSL                      10 hrs 2 mins       ████████████████████████░   94.86 % 
Windows                  32 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   05.14 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
JavaScript               3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 08/05/2026 18:56:19 UTC
<!--END_SECTION:waka-->
