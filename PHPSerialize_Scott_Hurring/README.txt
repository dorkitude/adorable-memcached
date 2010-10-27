Python implementation of PHP's native serialize() and unserialize() functions.

Scott Hurring
scott at hurring dot com
http://hurring.com/
Please be nice and send bugfixes and code improvements to me.

@version v0.4 BETA
@author Scott Hurring; scott at hurring dot com
@copyright Copyright (c) 2005 Scott Hurring
@license http://opensource.org/licenses/gpl-license.php GNU Public License

Most recent version can be found at:
http://hurring.com/code/python/serialize/

=====================================================================

Unlike modules that make use of language-specific binary formats, the
output of serialize() is an ASCII string, meaning you can easily
manipulate it as you would any other string, i.e. sticking it
into a URL, a database, a file, etc...

Taken along with my perl serialize implementation, this code will
enable you to transfer data between PHP, Python, and Perl using PHP's
data serialization format.

To serialize:
	# Create an instance of the serialize engine
	s = PHPSerialize()
	# serialize some python data into a string
	serialized_string = s.serialize(python_data)

To unserialize:
	# Create an instance of the unserialize engine
	u = PHPUnserialize()
	# unserialize some string into python data
	python_data = u.unserialize(serialized_string)

PHP Serialization Format:
	NULL		N;
	Boolean		b:1;			b:$data;
	Integer		i:123;			i:$data;
	Double		d:1.23;			d:$data;
	String		s:5:"Hello"		s:$length:"$data";
	Array		a:1:{i:1;i:2}		a:$key_count:{$key;$value}
						$value can be any data type

Supported Python Types:
	Serializing:
	None, bool, int, float, long, string, dict, tuple*, list*

	Unserializing:
	None, bool, int, float, string, dict

*tuple and list are handled special becuase PHP only has one array
type "array()", which is analagous to Python Dicts.  When you try to
serialize a python tuple or list, it's automagically converted into a
dictionary with keys numbered from 0 up.

Type Translation Table:
	(Py)	(serialize)	(PHP)	    (unserialize)  (Py)
	None 	=>		NULL 			=> None
	bool 	=>		bool			=> bool
	int 	=>		int 			=> int
	float 	=>		double			=> float
	long 	=>		double			=> float
	string 	=>		string			=> string
	tuple 	=>		array			=> dict
	list 	=>		array			=> dict
	dict 	=>		array			=> dict


=====================================================================

Warning:

This code comes with absolutely NO warranty... it is a quick hack
that i sometimes work on in my spare time.  This code may or may
not melt-down your computer and give you nonsensical output.

Please, do not use this code in a production enviornment until
you've thoroughly tested it.

=====================================================================
