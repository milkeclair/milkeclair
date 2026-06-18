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
![Code Time](http://img.shields.io/badge/Code%20Time-2%2C577%20hrs%2040%20mins-blue?style=flat)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-616.78%20thousand%20lines%20of%20code-blue?style=flat)

**I'm a Night 🦉** 

```text
🌞 Morning                1373 commits        █████░░░░░░░░░░░░░░░░░░░░   21.06 % 
🌆 Daytime                1560 commits        ██████░░░░░░░░░░░░░░░░░░░   23.93 % 
🌃 Evening                1886 commits        ███████░░░░░░░░░░░░░░░░░░   28.93 % 
🌙 Night                  1701 commits        ███████░░░░░░░░░░░░░░░░░░   26.09 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   831 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.75 % 
Tuesday                  899 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.79 % 
Wednesday                641 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.83 % 
Thursday                 834 commits         ███░░░░░░░░░░░░░░░░░░░░░░   12.79 % 
Friday                   1208 commits        █████░░░░░░░░░░░░░░░░░░░░   18.53 % 
Saturday                 729 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.18 % 
Sunday                   1378 commits        █████░░░░░░░░░░░░░░░░░░░░   21.13 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Java                     10 hrs 46 mins      ██████████░░░░░░░░░░░░░░░   41.67 % 
Bash                     7 hrs               ███████░░░░░░░░░░░░░░░░░░   27.12 % 
Markdown                 3 hrs 1 min         ███░░░░░░░░░░░░░░░░░░░░░░   11.68 % 
Other                    1 hr 28 mins        █░░░░░░░░░░░░░░░░░░░░░░░░   05.69 % 
Ruby                     1 hr                █░░░░░░░░░░░░░░░░░░░░░░░░   03.92 % 

💻 Operating System: 
WSL                      24 hrs 41 mins      ████████████████████████░   95.52 % 
Mac                      1 hr 9 mins         █░░░░░░░░░░░░░░░░░░░░░░░░   04.48 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     9 repos             ████████████░░░░░░░░░░░░░   47.37 % 
TypeScript               2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Shell                    2 repos             ███░░░░░░░░░░░░░░░░░░░░░░   10.53 % 
Java                     1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   05.26 % 
```




 Last Updated on 18/06/2026 19:17:55 UTC
<!--END_SECTION:waka-->
