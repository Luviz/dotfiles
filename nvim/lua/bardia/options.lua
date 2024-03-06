local options = {
  clipboard = "unnamedplus",
  relativenumber = true,
  number = true,

  showtabline = 2,
  expandtab = true,
  tabstop = 2,
  shiftwidth = 2,
}

for k, v in pairs(options) do 
  vim.opt[k]=v
end
