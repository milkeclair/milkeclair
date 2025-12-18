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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C837%20hrs%2040%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-380.9%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                913 commits         █████░░░░░░░░░░░░░░░░░░░░   21.85 % 
🌆 Daytime                940 commits         ██████░░░░░░░░░░░░░░░░░░░   22.49 % 
🌃 Evening                1251 commits        ███████░░░░░░░░░░░░░░░░░░   29.94 % 
🌙 Night                  1075 commits        ██████░░░░░░░░░░░░░░░░░░░   25.72 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   561 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.42 % 
Tuesday                  589 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.09 % 
Wednesday                474 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.34 % 
Thursday                 566 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.54 % 
Friday                   743 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.78 % 
Saturday                 420 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.05 % 
Sunday                   826 commits         █████░░░░░░░░░░░░░░░░░░░░   19.77 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     27 hrs 11 mins      ██████████████░░░░░░░░░░░   57.57 % 
TypeScript               10 hrs 6 mins       █████░░░░░░░░░░░░░░░░░░░░   21.41 % 
Markdown                 2 hrs 38 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.58 % 
Other                    2 hrs 35 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.48 % 
Bash                     1 hr 59 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   04.22 % 

💻 Operating System: 
WSL                      38 hrs 28 mins      ████████████████████░░░░░   81.46 % 
Mac                      8 hrs 45 mins       █████░░░░░░░░░░░░░░░░░░░░   18.54 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   47.62 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   19.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   14.29 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   09.52 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
```




 Last Updated on 18/12/2025 18:44:38 UTC
<!--END_SECTION:waka-->
