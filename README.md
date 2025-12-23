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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C868%20hrs%2041%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-383.7%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                919 commits         █████░░░░░░░░░░░░░░░░░░░░   21.73 % 
🌆 Daytime                962 commits         ██████░░░░░░░░░░░░░░░░░░░   22.74 % 
🌃 Evening                1272 commits        ████████░░░░░░░░░░░░░░░░░   30.07 % 
🌙 Night                  1077 commits        ██████░░░░░░░░░░░░░░░░░░░   25.46 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   570 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.48 % 
Tuesday                  597 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.11 % 
Wednesday                474 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.21 % 
Thursday                 566 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.38 % 
Friday                   756 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.87 % 
Saturday                 420 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.93 % 
Sunday                   847 commits         █████░░░░░░░░░░░░░░░░░░░░   20.02 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     43 hrs 34 mins      █████████████████████░░░░   85.90 % 
Other                    1 hr 48 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   03.58 % 
ERB                      1 hr 35 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   03.13 % 
TypeScript               1 hr 17 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   02.56 % 
JavaScript               1 hr 1 min          █░░░░░░░░░░░░░░░░░░░░░░░░   02.02 % 

💻 Operating System: 
WSL                      48 hrs 24 mins      ████████████████████████░   95.45 % 
Mac                      2 hrs 18 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   04.55 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   47.62 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   19.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   14.29 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   09.52 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
```




 Last Updated on 23/12/2025 18:44:11 UTC
<!--END_SECTION:waka-->
