var gulp = require('gulp');
var exec = require('child_process').exec;

var Paths = {
    template_src:'templates/*.html',
};

// run server
gulp.task( 'server_start', function() {
    exec('bash start.sh', function (err, stdout, stderr) {
        console.log(stdout);
        console.log(stderr);
        if(err) return cb(err);
        cb();
    });
});

gulp.task('watch',['server_start'],function(){
    gulp.watch([Paths.template_src],[]);
});

gulp.task('default', ['server_start','watch']);
