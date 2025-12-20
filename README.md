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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C841%20hrs%2018%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-381.2%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                919 commits         █████░░░░░░░░░░░░░░░░░░░░   21.92 % 
🌆 Daytime                947 commits         ██████░░░░░░░░░░░░░░░░░░░   22.59 % 
🌃 Evening                1251 commits        ███████░░░░░░░░░░░░░░░░░░   29.84 % 
🌙 Night                  1075 commits        ██████░░░░░░░░░░░░░░░░░░░   25.64 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   561 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.38 % 
Tuesday                  589 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.05 % 
Wednesday                474 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.31 % 
Thursday                 566 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.50 % 
Friday                   756 commits         █████░░░░░░░░░░░░░░░░░░░░   18.03 % 
Saturday                 420 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.02 % 
Sunday                   826 commits         █████░░░░░░░░░░░░░░░░░░░░   19.70 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     27 hrs 59 mins      ██████████████████░░░░░░░   72.00 % 
TypeScript               5 hrs 4 mins        ███░░░░░░░░░░░░░░░░░░░░░░   13.07 % 
Other                    3 hrs 2 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   07.81 % 
YAML                     43 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.87 % 
Bash                     39 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.71 % 

💻 Operating System: 
WSL                      31 hrs 40 mins      ████████████████████░░░░░   81.47 % 
Mac                      7 hrs 12 mins       █████░░░░░░░░░░░░░░░░░░░░   18.53 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   47.62 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   19.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   14.29 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   09.52 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
```




 Last Updated on 20/12/2025 18:40:11 UTC
<!--END_SECTION:waka-->
