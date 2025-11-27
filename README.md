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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C692%20hrs%2051%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-326.8%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                774 commits         █████░░░░░░░░░░░░░░░░░░░░   20.20 % 
🌆 Daytime                898 commits         ██████░░░░░░░░░░░░░░░░░░░   23.44 % 
🌃 Evening                1136 commits        ███████░░░░░░░░░░░░░░░░░░   29.65 % 
🌙 Night                  1023 commits        ███████░░░░░░░░░░░░░░░░░░   26.70 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   491 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.82 % 
Tuesday                  551 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.38 % 
Wednesday                446 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.64 % 
Thursday                 540 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.10 % 
Friday                   691 commits         █████░░░░░░░░░░░░░░░░░░░░   18.04 % 
Saturday                 363 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.48 % 
Sunday                   749 commits         █████░░░░░░░░░░░░░░░░░░░░   19.55 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Bash                     16 hrs 7 mins       ██████████░░░░░░░░░░░░░░░   38.68 % 
Ruby                     15 hrs 5 mins       █████████░░░░░░░░░░░░░░░░   36.19 % 
Markdown                 3 hrs 56 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   09.45 % 
TypeScript               3 hrs 47 mins       ██░░░░░░░░░░░░░░░░░░░░░░░   09.08 % 
Other                    2 hrs 12 mins       █░░░░░░░░░░░░░░░░░░░░░░░░   05.29 % 

💻 Operating System: 
WSL                      39 hrs 59 mins      ████████████████████████░   95.88 % 
Mac                      1 hr 42 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   04.12 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            █████████████░░░░░░░░░░░░   52.63 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   21.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   15.79 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
Batchfile                1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 27/11/2025 18:41:44 UTC
<!--END_SECTION:waka-->
