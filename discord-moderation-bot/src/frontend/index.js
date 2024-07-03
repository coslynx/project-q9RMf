import discord from 'discord.js';

const client = new discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', async (message) => {
  if (message.author.bot) return;

  if (message.content === '!ping') {
    message.channel.send('Pong!');
  }
});

client.login('your_token_here');

export default client;