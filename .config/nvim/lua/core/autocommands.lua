--
-- AutoCommands
--

local all_files_augroup = vim.api.nvim_create_augroup('allfiles', { clear = true })

--[[ TODO: Cehck why not working
vim.api.nvim_create_autocmd({'BufReadPost', 'FileReadPost'}, {
  group = all_files_augroup,
  pattern = '*',
  command = 'normal zR'
})
]]


--[[ TODO: Check why mot working
vim.api.nvim_create_autocmd({'BufEnter','BufAdd','BufNew','BufNewFile','BufWinEnter'}, {
  group = all_files_augroup,
  callback = function()
    vim.opt.foldmethod     = 'expr'
    vim.opt.foldexpr       = 'nvim_treesitter#foldexpr()'
  end
})
]]
