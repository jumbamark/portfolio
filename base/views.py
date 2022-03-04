from django.shortcuts import render, redirect
from .models import Project, Skill, Message, Endorsement, Comment
from .forms import ProjectForm, MessageForm, SkillForm, EndorsementForm, CommentForm, QuestionForm
from django.contrib import messages


# Create your views here.


# rendering our home template
def homePage(request):
    projects = Project.objects.all()
    skills = Skill.objects.exclude(body="")
    otherSkills = Skill.objects.filter(body="")
    form = MessageForm()
    endorsements = Endorsement.objects.filter(approved=True)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was succesfully sent")

    context = {
        "Projects": projects,
        "Skills": skills,
        "Others": otherSkills,
        "Form": form,
        "Endorsements": endorsements,
    }
    return render(request, "base/home.html", context)


# creating a view for the projects template
def projectPage(request, pk):
    project = Project.objects.get(id=pk)  # querying the object by its id
    count = Comment.objects.count()

    comments = project.comment_set.all().order_by('-created')

    Form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # when I submit a comment where is it gonna get assigned to
            # we're getting the object withiut actually officially saving that form
            comment = form.save(commit=False)
            comment.project = project  # assigning it to the project we created up there
            comment.save()
            messages.success(request, "Your comment was succesfully added")

    context = {
        "Project": project,
        "Count": count,
        "Comments": comments,
        "Forms": Form,
    }

    return render(request, "base/projects.html", context)


# creating  a view for project_form template
def addProject(request):
    form = ProjectForm()

    # If request method is equal to POST, submit this form
    if request.method == "POST":
        # pass in the original post data and any files send from the frontend(we're sending files right to enctype)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "Form": form,
    }
    return render(request, "base/project_form.html", context)


# creating  a view for an edit button
def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        # we neeed to pass in this instance and tell it which instance we're updating to avoid re-submission of the same project
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "Form": form,
    }
    return render(request, "base/project_form.html", context)


# rendering a view for inbox.html
def inboxPage(request):
    message = Message.objects.all().order_by("-is_read")
    unreadCount = Message.objects.filter(
        is_read=False).count()  # unread messages
    context = {
        "inbox": message,
        "UnreadMessages": unreadCount,
    }
    return render(request, "base/inbox.html", context)


# rendering a view for message..html
def messagePage(request, pk):
    inbox = Message.objects.get(id=pk)
    # when you open up this view, the email automatically gets marked as read
    inbox.is_read = True
    inbox.save()
    context = {
        "Inbox": inbox,
    }
    return render(request, "base/message.html", context)


# rendering a view for skill_form.html
def addSkill(request):
    form = SkillForm()

    if request.method == "POST":
        form = SkillForm(request.POST)
        form.save()
        messages.success(request, "Your skill was succesfully added")
        return redirect("home")

    context = {
        "skillForm": form,
    }

    return render(request, "base/skill_form.html", context)


def addEndorsement(request):
    form = EndorsementForm()
    if request.method == "POST":
        form = EndorsementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Thank you, your endorsement was succesfully added")
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "base/endorsements_form.html", context)


def donationPage(request):
    return render(request, "base/donation.html")


# renedering chart.htnl
def chartPage(request):
    Form = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for voting")
            return redirect("chart")
    return render(request, "base/chart.html", {"Form": Form})
