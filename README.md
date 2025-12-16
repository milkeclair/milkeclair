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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C817%20hrs%2059%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-379.2%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                902 commits         █████░░░░░░░░░░░░░░░░░░░░   21.71 % 
🌆 Daytime                930 commits         ██████░░░░░░░░░░░░░░░░░░░   22.39 % 
🌃 Evening                1247 commits        ████████░░░░░░░░░░░░░░░░░   30.02 % 
🌙 Night                  1075 commits        ██████░░░░░░░░░░░░░░░░░░░   25.88 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   561 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.51 % 
Tuesday                  589 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.18 % 
Wednesday                459 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.05 % 
Thursday                 556 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.38 % 
Friday                   743 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.89 % 
Saturday                 420 commits         ███░░░░░░░░░░░░░░░░░░░░░░   10.11 % 
Sunday                   826 commits         █████░░░░░░░░░░░░░░░░░░░░   19.88 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     13 hrs 18 mins      ██████████░░░░░░░░░░░░░░░   41.99 % 
TypeScript               8 hrs 53 mins       ███████░░░░░░░░░░░░░░░░░░   28.05 % 
Markdown                 4 hrs 37 mins       ████░░░░░░░░░░░░░░░░░░░░░   14.58 % 
Bash                     1 hr 39 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   05.21 % 
Other                    1 hr 15 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   03.97 % 

💻 Operating System: 
WSL                      19 hrs 58 mins      ████████████████░░░░░░░░░   63.02 % 
Mac                      11 hrs 43 mins      █████████░░░░░░░░░░░░░░░░   36.98 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   47.62 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   19.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   14.29 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   09.52 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
```




 Last Updated on 16/12/2025 18:44:40 UTC
<!--END_SECTION:waka-->
