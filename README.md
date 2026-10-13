```ruby


Milkeclair.profile do
  desc :beginner
  like :beautiful_dsl
end

class Milkeclair
  include Singleton

  attr_reader :_desc, :_like

  def self.profile(&block)
    block_given? ? instance.instance_exec(&block) : instance
  end

  def desc(*args)
    me = :"@_#{__callee__}"
    args.empty? ? p(instance_variable_get(me)) : instance_variable_set(me, args)
  end
  alias_method :like, :desc
end
```
</details>

