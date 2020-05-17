# Source: *Feeling Good*
# libgen: https://libgen.is/book/index.php?md5=C125D95C465F61F9D97A1F7A8709B82A
# page 49-50 of the pdf.

# Note: to create a bash utility, add the following:
# alias bdi='ruby /home/nuno/Documents/Workspace/WEBDEV/RubyOnRails/BDI.rb'
# (or whatever the full path to this file is)
# to the end of your .bashrc file,
# which should be in your ~ (home) folder (check with ls -a)

questions = [
"Feeling sad or down in the dumps",
"Feeling unhappy or blue",
"Crying spells or tearfulness",
"Feeling discouraged",
"Feeling hopeless",
"Low self-esteem",
"Feeling worthless or inadequate",
"Guilt or shame",
"Criticizing yourself or blaming yourself",
"Difficulty making decisions",
"Loss of interest in family, friends or colleagues",
"Loneliness",
"Spending less time with family or friends",
"Loss of motivation",
"Loss of interest in work or other activities",
"Avoiding work or other activities",
"Loss of pleasure or satisfaction in life",
"Feeling tired",
"Difficulty sleeping or sleeping too much",
"Decreased or increased appetite",
"Loss of interest in sex",
"Worrying about your health",
"Do you have any suicidal thoughts?",
"Would you like to end your life?",
"Do you have a plan for harming yourself?"
]

fileName = "/home/nuno/Documents/Workspace/WEBDEV/RubyOnRails/ BDI.txt"
fileTargetStream = open(fileName, "a")

total = 0
scoreList = []

instructions = """
Write a number to indicate how much you have experienced each symptom today
\t* 0 - Not at all
\t* 1 - Somewhat
\t* 2 - Moderately
\t* 3 - A lot
\t* 4 - Extremely

"""

puts instructions

for question in questions
  puts question
  print "> "
  answer = $stdin.gets.chomp.to_i
  total+=answer
  scoreList.push(answer)
end

scoreListPretty = scoreList.join(', ')
puts "Total: #{total}"
puts "List: #{scoreListPretty}"

fileTargetStream.write("\n\nTimestamp: #{Time.now}")
fileTargetStream.write("\nTotal: #{total}")
fileTargetStream.write("\nList: #{scoreListPretty}")

fileTargetStream.close
