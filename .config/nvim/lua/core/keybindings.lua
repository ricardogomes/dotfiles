--
-- Neovim Core Keybingings
--

local map = vim.api.nvim_set_keymap
local opts = { noremap = true, silent = true }


-- Leader
map('', '<Space>', 'Nop', opts)
vim.g.mapleader         = ' '
vim.g.mapgloballeader   = ' '

-- Window Managment
map('n', '<C-Up>', '<C-w>k', opts)
map('n', '<C-Down>', '<C-w>j', opts)
map('n', '<C-Left>', '<C-w>h', opts)
map('n', '<C-Right>', '<C-w>l', opts)

map('n', '<C-S-Up>', ':resize +2<CR>', opts)
map('n', '<C-S-Down>', ':resize -2<CR>', opts)
map('n', '<C-S-Left>', ':vertical resize -2<CR>', opts)
map('n', '<C-S-Right>', ':vertical resize +2<CR>', opts)

-- Buffer Management
map('n', '<S-Right>', ':bnext<CR>', opts)
map('n', '<S-Left>', ':bprevious<CR>', opts)
map('n', '<C-s>', ':w<CR>', { noremap = true })
map('n', '<C-x>', ':source %<CR>', opts)

-- Editing
map('v', '>', '<gv', opts)
map('v', '<', '>gv', opts)

map('v', '<A-Up>', ":move .-2<CR>==", opts)
map('v', '<A-Down>', ":move .+2<CR>==", opts)

map('x', '<A-Down>', ":move '>+2<CR>gv-gv", opts)
map('x', '<A-Up>', ":move '>-2<CR>gv-gv", opts)




