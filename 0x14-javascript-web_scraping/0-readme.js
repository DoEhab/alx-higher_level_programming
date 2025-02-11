#!/usr/bin/node

if (process.argv[2]) {
  try {
    const fileName = process.argv[2];
    const fileStream = require('fs');
    const fileContent = fileStream.readFileSync(fileName, 'utf-8');
    fileContent.split(/\r?\n/).forEach(line => {
      console.log(line);
    });
  } catch (err) {
    if (err.code === 'ENOENT') {
      console.log(
        {
          error: err.message,
          errno: err.errno,
          code: err.code,
          syscall: err.syscall,
          path: err.path
        });
    }
  }
}
