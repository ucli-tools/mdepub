-- Pandoc Lua filter to create custom 'Part' pages.

function Header(el)
  -- Get the text of the header
  local header_text = pandoc.utils.stringify(el.content)

  -- Check if the header text starts with 'Part '
  if string.match(header_text, '^Part ') then
    -- If it's a Part header, wrap it in a Div with the class 'part-page'
    -- This allows for special styling in the CSS.
    return pandoc.Div(el, {class = 'part-page'})
  end

  -- For all other headers, return them unchanged
  return el
end
