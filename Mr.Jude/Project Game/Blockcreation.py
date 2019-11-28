#%%
from Block import block

def create_wall(game, blocks):
     for row_number in range(5):
         for block_number in range(5):
             create_block(game, blocks, block_number, row_number)


def create_block(game, blocks, block_number, row_number):
    Block = block(game)
    Block_width = Block.rect.width
    Block.x = Block_width + 1.5 * Block_width * block_number
    Block.rect.x = Block.x
    Block.rect.y = Block.rect.height + 2 * Block.rect.height * row_number
    blocks.add(Block)