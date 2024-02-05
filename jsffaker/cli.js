const jsf = require('json-schema-faker');
const yargs = require('yargs');

// Define CLI options using yargs
const argv = yargs
  .option('schema', {
    alias: 's',
    describe: 'JSON schema to generate data',
    demandOption: true, // Make it a required option
    type: 'string'
  })
  .help()
  .argv;

// Function to generate JSON based on the provided schema
function generateJson(schema) {
  const options = {
    minItems: 1,
    maxItems: 1
  };

  return jsf.generate(schema, options);
}

// Main CLI logic
const generatedJson = generateJson(JSON.parse(argv.schema));
console.log(JSON.stringify(generatedJson, null, 2));