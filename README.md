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
![Code Time](http://img.shields.io/badge/Code%20Time-1%2C890%20hrs%2034%20mins-blue)

![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%27ve%20Written-386.9%20thousand%20lines%20of%20code-blue)

**I'm a Night 🦉** 

```text
🌞 Morning                922 commits         █████░░░░░░░░░░░░░░░░░░░░   21.74 % 
🌆 Daytime                964 commits         ██████░░░░░░░░░░░░░░░░░░░   22.73 % 
🌃 Evening                1276 commits        ████████░░░░░░░░░░░░░░░░░   30.08 % 
🌙 Night                  1080 commits        ██████░░░░░░░░░░░░░░░░░░░   25.46 % 
```
📅 **I'm Most Productive on Sunday** 

```text
Monday                   570 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.44 % 
Tuesday                  600 commits         ████░░░░░░░░░░░░░░░░░░░░░   14.14 % 
Wednesday                478 commits         ███░░░░░░░░░░░░░░░░░░░░░░   11.27 % 
Thursday                 567 commits         ███░░░░░░░░░░░░░░░░░░░░░░   13.37 % 
Friday                   756 commits         ████░░░░░░░░░░░░░░░░░░░░░   17.82 % 
Saturday                 422 commits         ██░░░░░░░░░░░░░░░░░░░░░░░   09.95 % 
Sunday                   849 commits         █████░░░░░░░░░░░░░░░░░░░░   20.01 % 
```


📊 **This Week I Spent My Time On** 

```text
💬 Programming Languages: 
Ruby                     12 hrs 54 mins      ██████████████████████░░░   88.35 % 
JavaScript               44 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   05.13 % 
ERB                      43 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   04.92 % 
TypeScript               13 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   01.51 % 
Other                    0 secs              ░░░░░░░░░░░░░░░░░░░░░░░░░   00.08 % 

💻 Operating System: 
WSL                      14 hrs 17 mins      ████████████████████████░   97.85 % 
Mac                      18 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   02.15 % 
```

**I Mostly Code in Ruby** 

```text
Ruby                     10 repos            ████████████░░░░░░░░░░░░░   47.62 % 
JavaScript               4 repos             █████░░░░░░░░░░░░░░░░░░░░   19.05 % 
Shell                    3 repos             ████░░░░░░░░░░░░░░░░░░░░░   14.29 % 
TypeScript               2 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   09.52 % 
CSS                      1 repo              █░░░░░░░░░░░░░░░░░░░░░░░░   04.76 % 
```




 Last Updated on 31/12/2025 18:43:12 UTC
<!--END_SECTION:waka-->
